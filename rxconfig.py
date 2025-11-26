import reflex as rx

DEPLOY_URL = "https://adviento.dev"

config = rx.Config(
    app_name="adeviento_web",
    deploy_url=DEPLOY_URL,
    plugins=[rx.plugins.SitemapPlugin()],
    show_built_with_reflex=False,
)
