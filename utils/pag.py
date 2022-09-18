from discord.ext import menus

class Pag(menus.MenuPages):
    def __init__(self, *, source: menus.PageSource, **kwargs):
        super().__init__(source, **kwargs)
