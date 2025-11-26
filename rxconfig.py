import reflex as rx

config = rx.Config(
    app_name="adeviento_web",
    backend_port=None,
    deploy_url=None,
    plugins=[rx.plugins.SitemapPlugin()],
    show_built_with_reflex=False,
)
