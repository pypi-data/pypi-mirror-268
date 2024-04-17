import os

import dotenv
import uvicorn

dotenv.load_dotenv(".env")

def main():
    uvicorn.run(
        "ntp_manager.webapp:app", 
        host=os.getenv('web_host', '0.0.0.0'), 
        port=int(os.getenv('web_port', '7996')), reload=False
    )

if __name__ == "__main__":
    main()
