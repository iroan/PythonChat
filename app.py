import aiopg
import tornado
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.locks
import tornado.httpserver
from tornado.options import define
from tornado.options import options

define("port",default=8888,help="服务器运行的端口",type=int)
define("db_host",default="127.0.0.1",help="数据库运行的ip地址")
define("db_port",default=5432,help="数据库运行的端口")
define("db_database",default="exampledb",help="数据库操作的数据库名字")
define("db_user",default="dbuser",help="登录数据库的用户名")
define("db_password",default="iroanDBS47",help="登录数据库的密码")

class BaseHandler(tornado.web.RequestHandler):
    pass

class HomeHandler(BaseHandler):
    pass

class ArchiveHandler(BaseHandler):
    pass

class FeedHandler(BaseHandler):
    pass

class EntryHandler(BaseHandler):
    pass
class CompaseHandler(BaseHandler):
    pass
class AuthCreateHandler(BaseHandler):
    pass
class AuthLoginHandler(BaseHandler):
    pass
class AuthLogoutHandler(BaseHandler):
    pass

class Application(tornado.web.Application):
    def __init__(self,db):
        self.db = db
        handlers = [
            (r"/",HomeHandler),
            (r"/archive",ArchiveHandler),
            (r"/feed",FeedHandler),
            (r"/entry/(^/]+)",EntryHandler),
            (r"/compose",CompaseHandler),
            (r"/auth/create",AuthCreateHandler),
            (r"/auth/login",AuthLoginHandler),
            (r"/auth/logout",AuthLogoutHandler),
        ]
async def maybe_create_tables(db):
    try:
        with (await db.cursor()) as target:
            await target.execute("select count(*) from entries limit 1")
            await target.fetchone()
    except psycopg2.ProgramingError:
        with open("schema.sql") as f:
            schema = f.read()
        with (await db.cursor()) as target:
            await target.execute(schema)

async def main():
    tornado.options.parse_command_line()
    # 解析命令行
    async with aiopg.create_pool(
        host = options.db_host,
        port = options.db_port,
        user = options.db_user,
        password = options.db_password,
        dbname = options.db_database,
    )as db:
        await maybe_create_tables(db)
        app = Application(db)
        app.listen(options.port)
        shutdown_event = tornado.locks.Event()
        print(options.print_help())
        await shutdown_event.wait()
if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
