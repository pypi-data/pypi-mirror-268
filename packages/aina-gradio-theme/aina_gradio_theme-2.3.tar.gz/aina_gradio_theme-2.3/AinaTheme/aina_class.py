from gradio.themes.utils import colors, fonts, sizes
from gradio.themes import Soft
from typing import Iterable

class Aina(Soft):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.indigo,
        secondary_hue: colors.Color | str = colors.indigo,
        neutral_hue: colors.Color | str = colors.gray,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_md,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Montserrat"),
            "ui-sans-serif",
            "system-ui",
            "sans-serif",
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "Consolas",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name = "aina"
        super().set(
            block_title_text_color="black",
            block_label_text_color="black",
            block_label_text_weight=600,
            block_title_text_weight=600,
            block_title_background_fill="transparent",
            block_label_background_fill="transparent",
            input_shadow="rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px",
            input_shadow_focus="rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 2px",
        )

