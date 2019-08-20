from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'user_page.login'
login_manager.login_message = '请先登录'


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name,
                                          template_folder=template_folder,
                                          root_path=root_path,
                                          static_folder=None)
        self.config.from_pyfile('config/base_setting.py' )
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])

        db.init_app( self )
        login_manager.init_app(self)


db = SQLAlchemy()
app = Application(__name__,
                  template_folder=os.getcwd() + "/web/templates/",
                  root_path=os.getcwd())
manager = Manager(app)

from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')



