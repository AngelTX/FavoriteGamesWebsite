import fresh_tomatoes
import media

# Initiate all of the instances of Games i'm going to use
# with a name, image, and youtube link.
majorasMask = media.Game(
    "The Legend of Zelda: Majora's Mask",
    "https://images3.alphacoders.com/612/thumb-1920-612032.jpg",
    "https://www.youtube.com/watch?v=Hj6cXziHpjQ"
    )

limbo = media.Game(
    "Limbo",
    "https://www.keengamer.com/Image/Image/16027",
    "https://www.youtube.com/watch?v=irBwfZ8iAYU"
    )

braid = media.Game(
    "Braid",
    "https://www.walldevil.com/wallpapers/a15/high-resolution-ebypf.jpg",
    "https://www.youtube.com/watch?v=uqtSKkyJgFM"
    )

steamworldHeist = media.Game(
    "Steamworld Heist",
    "https://i.ytimg.com/vi/epv2WLrWpXU/maxresdefault.jpg",
    "https://www.youtube.com/watch?v=mV5_Hp3kG7U"
    )

bastion = media.Game(
    "Bastion",
    "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/items/107100/c566a78138dc070ded3c34f4bf91a9055a65282a.jpg",  # NOQA
    "https://www.youtube.com/watch?v=mX48y24t9iU"
    )

owlboy = media.Game(
    "Owlboy",
    "http://www.owlboygame.com/images/Art/Full/Horizontal%20poster%20Logos.png",  # NOQA
    "https://www.youtube.com/watch?v=p9VwGaycmCQ"
    )

dontStarve = media.Game(
    "Don't Starve",
    "https://www.klei.com/sites/default/files/styles/thumb/public/games/dont-starve/video-thumbs/920x680large-tile.jpg?itok=CZEkMT3o",  # NOQA
    "https://www.youtube.com/watch?v=fXP4_2qRHng"
    )

# consolodate all my instances of  Games inside an array.
games = [majorasMask, limbo, braid, steamworldHeist, bastion, owlboy]

# Run fresh_tomatoes taking my array of games as an argument.
fresh_tomatoes.open_games_page(games)
