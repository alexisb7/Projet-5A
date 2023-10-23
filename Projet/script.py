import qrcode
from qrcode.constants  import ERROR_CORRECT_L
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def QRCode_generator(name):
    qr = qrcode.QRCode(
        version=3,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data('https://forms.office.com/Pages/ResponsePage.aspx?id=ICXHB0XmeUaPVdxhHJdaAgVVBT2VFj9PumthlDIpVhFUN1hUSExESTNQSVhDUVNZTTZERkc2R0s3Qy4u')
    qr.make(fit=True)

    img = qr.make_image(fill_color="White", back_color="Transparent", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask(back_color=(242,242,244),edge_color=(147,0,255),center_color=(186,0,0))).convert("RGB")
    name = name.upper()
    file = "./static/img/QR_CODE_" + name + "_FORUM_CARRIERE_2022.png"
    img.save(file)
    return file

def QRCode_generator_logo(name, logo):
    qr = qrcode.QRCode(
        version=3,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data('https://forms.office.com/Pages/ResponsePage.aspx?id=ICXHB0XmeUaPVdxhHJdaAgVVBT2VFj9PumthlDIpVhFUN1hUSExESTNQSVhDUVNZTTZERkc2R0s3Qy4u')
    qr.make(fit=True)

    img = qr.make_image(fill_color="White", back_color="Transparent", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask(back_color=(242,242,244),edge_color=(147,0,255),center_color=(186,0,0))).convert("RGB")

    logo_display = Image.open(logo)
    logo_display.thumbnail((60,60))
    log_pos = ((img.size[0]-logo_display.size[0])//2, (img.size[1]-logo_display.size[1])//2)
    img.paste(logo_display, log_pos)
    name = name.upper()
    file = "./static/img/QR_CODE_" + name + "_FORUM_CARRIERE_2022.png"
    img.save(file)
    return file