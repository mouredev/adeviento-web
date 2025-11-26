import reflex as rx

config = rx.Config(
    app_name="adeviento_web",
    deploy_url=None,
    backend_port=None,
    api_url=None,
    plugins=[rx.plugins.SitemapPlugin()],
    show_built_with_reflex=False,
)
