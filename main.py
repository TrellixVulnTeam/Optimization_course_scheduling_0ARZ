import gui
import error_handler
import data
import db_controller
import admin
import user
import schedule
appData = data.Data()
error_handler = error_handler.ErrorHandler()
gui.welcome_page(appData)
if appData.user_args != appData.ADMIN_KEY:
    status = error_handler.args_controller(appData)
    if status == 0 :
        exit(status)
    appData.set_db_controller(db_controller.DataBaseController())
    user.User(appData).run()
else:
    appData.set_db_controller(db_controller.DataBaseController())
    admin.Admin(appData).run()