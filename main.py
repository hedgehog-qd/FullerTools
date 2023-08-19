from quart import Quart
from quart import render_template
import config

app = Quart(__name__)


@app.errorhandler(404)
async def page_not_found(e):
    # NOTE: we set the 404 status explicitly
    return (await render_template('404.html'), 404)


@app.errorhandler(500)
async def page_not_found(e):
    # NOTE: we set the 500 status explicitly
    return (await render_template('500.html'), 500)


@app.template_global()
def appVersion() -> str:
    return config.app_version


@app.template_global()
def appName() -> str:
    return config.app_name


@app.route('/')
@app.route('/home')
async def home():
    return await render_template('home.html')


@app.route('/tag')
async def tags():
    return await render_template('tags.html')


@app.route('/viewtag')
async def viewtag():
    return await render_template('viewtag.html')


if __name__ == '__main__':
    app.run(port=5000)  # blocking call
