from flask_assets import Environment, Bundle

CSS_ASSETS = [
    'css/vendor/bootstrap.css',
    Bundle('css/application.scss',
           'css/programs.scss',
            filters='pyscss', output='css/compiled-scss.css')
]

JS_ASSETS = [
    "js/vendor/jqeury-1.11.1.min.js",
    "js/vendor/bootstrap.js",
    "js/application.js",
    "js/smooth-scroll.js"
]

def register_assets(app):
    assets = Environment(app)
    assets.debug = app.debug
    assets.auto_build = True
    assets.url = app.static_url_path

    css_all = Bundle(*CSS_ASSETS, filters='cssmin', output='css/bundle.min.css')
    js_all = Bundle(*JS_ASSETS, filters='rjsmin', output='js/all.min.js')

    assets.register('css_all', css_all)
    assets.register('js_all', js_all)
    app.logger.info("Registered assets...")
    return assets
