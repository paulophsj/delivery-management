def fill_scrollable_width(element):
    """Faz o conteúdo de uma Column scrollable acompanhar a largura do canvas,
    permitindo que elementos com expand_x ocupem todo o eixo X."""
    tkcf = element.TKColFrame
    canvas = tkcf.canvas
    frame_id = tkcf.frame_id

    canvas.bind(
        "<Configure>",
        lambda event: canvas.itemconfig(frame_id, width=event.width),
        add="+",
    )
