from aiohttp import web
from collections import defaultdict
from file_managers import DAILY_FILE_MANAGER


async def daily_file_write_log(request):
    """Writes log into files
    """
    data = await request.post()
    log_path = data.get('log_path', 'daily.log')
    msg = data.get('msg', '')
    day = data.get('day', '')
    if not DAILY_FILE_MANAGER.is_opened(log_path, day):
        DAILY_FILE_MANAGER.open(log_path)

    DAILY_FILE_MANAGER.write(log_path, msg)
    return web.HTTPCreated(text='ok')

app = web.Application()
app.add_routes([
    web.post('/daily-logger', daily_file_write_log),
])

if __name__ == "__main__":
    web.run_app(app, host='0.0.0.0', port=80)
