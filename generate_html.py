from jinja2 import Template

consoles = [
    "icon-lynx",
    "icon-lynx-2",
    "icon-lynx-game",
    "icon-famicom",
    "icon-famicom-game",
    "icon-famicom-pad",
    "icon-famicom-disk",
    "icon-famicom-zapper",
    "icon-gg-game",
    "icon-gba",
    "icon-gba-game",
    "icon-gbc",
    "icon-gbc-game",
    "icon-gg",
    "icon-gb",
    "icon-gb-game",
    "icon-sms",
    "icon-nec-game",
    "icon-nec-pad",
    "icon-nes",
    "icon-nec",
    "icon-nes-game",
    "icon-nes-pad",
    "icon-nes-zapper",
    "icon-neogeo",
    "icon-neogeo-game",
    "icon-neogeo-game-pad",
    "icon-nes-robot",
    "icon-sms-game",
    "icon-sms-pad",
    "icon-zillion",
    "icon-snes-scope",
    "icon-megacd",
    "icon-gen",
    "icon-gen2",
    "icon-gen-game",
    "icon-gen-pad",
    "icon-nomad",
    "icon-super-gb",
    "icon-snes",
    "icon-snes-game",
    "icon-snes-pad",
    "icon-super-famicom",
    "icon-super-famicom-game",
    "icon-super-famicom-pad",
    "icon-tgx16",
    "icon-tgx16-game",
    "icon-tgx16-pad",
]


template = Template(
    """
    {% for c in consoles %}
    <div class="thumbnail">
        <i class="retro {{c}}"> </i>
        <div class="caption body_post row-fluid">
            <div class="alert alert-success">{{c}}</div>
        </div>

    </div>
    {% endfor %}
    """
)

f = open("generated.html", "w")
f.write(
    template.render(consoles=consoles)
)
f.close()
