from collections import defaultdict
import json
from typing import AsyncGenerator, Generator
from dataclasses import dataclass
import geojson
import orjson
from serde import from_dict as from_dict
from shapely.geometry.base import BaseGeometry, GeometrySequence
from ntp_manager import parcellate
from pathlib import Path
import subprocess
import asyncio
import shlex
import random
import os
import tempfile
import zipfile


@dataclass
class MeltArgs:
    ntp_root: str
    bin_size: int

    ignore_regions        : str  = ''
    write_global_mask_npz : bool = False
    export_gene_count     : bool = False
    force_update          : bool = False


async def run_batch_ntp_melt(args: MeltArgs) -> AsyncGenerator[dict, None]:
    # python -m luigi_jobs.生成区域掩码 批量生成区域掩码 --ntp-root /mnt/90-connectome/finalNTP-layer4-parcellation91-106/C042-Ecc/ --force-update --bin-size 4
    cmd = [
        'poetry', 'run', 'python', '-m', 'luigi_jobs.生成区域掩码', '批量生成区域掩码',
        '--ntp-root', shlex.quote(str(args.ntp_root)), '--bin-size', str(args.bin_size),
    ]
    if args.force_update         : cmd.append('--force-update')
    if args.write_global_mask_npz: cmd.append('--write-global-mask-npz')
    if args.export_gene_count    : cmd.append('--export-gene-count')
    if args.ignore_regions       : 
        cmd.append('--ignore-regions')
        cmd.append(shlex.quote(args.ignore_regions))

    print(" ".join(cmd))
    current_env = os.environ
    _, temp_p = tempfile.mkstemp()
    current_env['NHP_DASHBOARD_NTP_MELT_PROCESS_FILE'] = temp_p

    cwd = '/home/myuan/projects/nhp-dashboard/backend'
    proc = await asyncio.create_subprocess_shell(
        " ".join(cmd), cwd=cwd, env=dict(current_env),
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )
    f = open(temp_p, 'r')
        
    while True:
        new_line = f.readline().strip()
        # print(f"{f.tell()} {new_line=}")
        if not new_line: 
            await asyncio.sleep(0.5)
        else:
            d: dict = json.loads(new_line)
            yield d
            # print('after yield')
            if d.get('status') == 'done' and d.get('log_file') == temp_p:
                # print(f'{temp_p} in {new_line}, break')
                break
        # print('loop end')
    # print('before proc.wait()')
    await proc.wait()

async def run_single_ntp_melt_and_get_zip(args: MeltArgs) -> str | None:
    g = run_batch_ntp_melt(args)

    logs = defaultdict(list)
    async for d in g:
        print(d)
        if (chip := d.get('chip')):
            logs[chip].append(d)

        if d.get('status') != 'single done':
            continue

        outputs: list = d['outputs']
        _, tmp_zip_path = tempfile.mkstemp(suffix='.zip')
        with zipfile.ZipFile(
            tmp_zip_path, 'w', 
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=3,
        ) as zip_f:
            for output in outputs:
                output = Path(output)
                if output.is_file():
                    zip_f.write(output, arcname=os.path.basename(output))
                    os.remove(output)
                elif output.is_dir():
                    for f in output.glob('**/*'):
                        if f.is_file():
                            zip_f.write(f, arcname=output.name / f.relative_to(output))
                            os.remove(f)

            zip_f.writestr(zinfo_or_arcname='log.txt', data=json.dumps(logs[chip]))
        print(f'zip file written to {tmp_zip_path}')

if __name__ == "__main__":
    async def main():
        # g = run_batch_ntp_melt(MeltArgs(
        #     ntp_root='/mnt/90-connectome/finalNTP-layer4-parcellation91-106/C042-Ecc/',
        #     force_update=True,
        #     bin_size=4,
        # ))

        # async for i in g:
        #     print(i)

        g = await run_single_ntp_melt_and_get_zip(MeltArgs(
            ntp_root='/mnt/90-connectome/finalNTP-layer4-parcellation91-106/C042-Ecc/',
            force_update=True,
            bin_size=4,
        ))
        print(g)


        

    asyncio.run(main())
