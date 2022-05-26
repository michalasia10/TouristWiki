if __name__ == '__main__':
    from main_app.src.core.server import run as main_app
    from mail_app.src.server import run as mail_app
    main_app()
    # mail_app()


