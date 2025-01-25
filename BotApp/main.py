import asyncio
from src.app.app import main



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Execution interrupted by user.")