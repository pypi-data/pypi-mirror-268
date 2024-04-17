import numpy as np
from matplotlib.path import Path


def n_pointed_star(*lengths, phi_0=1 / 4, base_radius=np.sqrt(2) / 6, mirror=True):
    """
    Args:
        *lengths: Normalized lengths of the arms
        base_radius: Radius of the base of the star
        mirror: wheter the arms are mirrored or not

    Examples:
        >>> import matplotlib.pyplot as plt
        >>> from rna.plotting.paths import n_pointed_star
        >>> _ = plt.plot(0, 0, marker=n_pointed_star(0.9, 0.5, 1), markersize=200, fillstyle='none')
        >>> _ = plt.plot(0, 0, marker=n_pointed_star(0.9, 0.5, 1, mirror=False), markersize=200, fillstyle='none')
        >>> _ = plt.plot(0, 0, marker=n_pointed_star(1, mirror=False), markersize=200, fillstyle='none')
        >>> _ = plt.show()
    """
    if not lengths:
        raise ValueError("Must provide at least one length")

    phi_0 *= 2 * np.pi
    if mirror:
        lengths = list(lengths) + list(lengths)
    n_arms = len(lengths)

    n_arms_was_1 = False
    if n_arms == 1:
        n_arms_was_1 = True
        n_arms = 4
    alpha = 2 * np.pi / n_arms
    base_length = np.cos(alpha / 2) * base_radius
    if n_arms_was_1:
        lengths = list(lengths) + [base_radius - base_length] * 3

    verts = []
    codes = []
    for i in range(n_arms * 2):
        arm_no = i // 2
        phi_i = phi_0 + alpha * (i - 1) / 2
        if i % 2 == 0:
            if base_radius is None:
                continue
            x = base_radius * np.cos(phi_i)
            y = base_radius * np.sin(phi_i)
        else:
            length = base_length + max(lengths[arm_no], 0)
            x = length * np.cos(phi_i)
            y = length * np.sin(phi_i)
        verts.append((x, y))
        if len(codes) == 0:
            codes.append(Path.MOVETO)
        else:
            codes.append(Path.LINETO)
    verts.append(verts[0])
    codes.append(Path.CLOSEPOLY)

    path = Path(verts, codes)
    return path


def from_curve(curve_func, num_points=40, connect=Path.LINETO):
    """
    Args:
        curve_func: Function that maps a number in [0, 1] to a point on the curve
        num_points: Number of points to generate
        connect: How to connect the points

    Examples:
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from rna.plotting.paths import from_curve

        >>> def fourrier_series(phi, coeffs=None):
        ...     if coeffs is None:
        ...         coeffs = [0, 1]
        ...     r_value = 0
        ...     z_value = 0
        ...     for n, a_n in enumerate(coeffs):
        ...         b_n = a_n if n % 2 == 1 else 0
        ...         r_value += a_n * np.cos(n * 2 * np.pi * phi)
        ...         z_value += b_n * np.sin(n * 2 * np.pi * phi)
        ...     return r_value, z_value

        >>> coeffs_gt_2 = [0.2, 0.1, 0.05, 0.05]
        >>> coeffs = [0.0, 1.0 - sum(coeffs_gt_2), *coeffs_gt_2]
        >>> path = from_curve(lambda x: fourrier_series(x, coeffs=coeffs))
        >>> _ = plt.plot(0, 0, marker=path, markersize=200, fillstyle='none')
        >>> _ = plt.show()

    """
    verts = []

    # Generate points along the curve
    for t in range(num_points + 1):
        t_normalized = t / num_points
        verts.append(curve_func(t_normalized))

    codes = [Path.MOVETO] + [connect] * num_points

    path = Path(verts, codes)
    return path


if __name__ == "__main__":
    # https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00159-020-00130-3/MediaObjects/159_2020_130_Fig14_HTML.png
    # https://www.google.com/search?q=matplotlib+colorbar+marker&tbm=isch&ved=2ahUKEwiD6J_VkqiCAxWE6qQKHTDmCVEQ2-cCegQIABAA&oq=matplotlib+colorbar+marker&gs_lcp=CgNpbWcQA1AAWABgAGgAcAB4AIABAIgBAJIBAJgBAKoBC2d3cy13aXotaW1n&sclient=img&ei=yRFFZcPfGoTVkwWwzKeIBQ&bih=1115&biw=1920&client=ubuntu&hs=ysZ#imgrc=XW-1sTvlVMmG8M&imgdii=K3GFldMw_Y2BWM
    import matplotlib.pyplot as plt
    from rna.plotting.colors import to_colors

    cmap = "viridis"
    marker_min = -1
    marker_max = 10
    vmin = 0
    vmax = 1
    multiply_x = 3

    ndim = 3
    norms = [plt.Normalize(marker_min, marker_max) for _ in range(ndim)]

    fig, (ax, ax1) = plt.subplots(ncols=2, gridspec_kw={"width_ratios": [15, 1]})
    fig.subplots_adjust(
        wspace=0.3,
    )

    artist = ax.plot(
        0.3,
        0.7,
        marker=n_pointed_star(-1, -0.1, 0, 1, base_radius=0.5),
        markersize=30,
        color="red",
    )
    artist = ax.plot(
        0.7,
        0.3,
        marker=n_pointed_star(0, 0, 0, 0, base_radius=0.5),
        markersize=30,
        color="red",
    )

    values = []
    artists = []
    for value in range(0, 11):
        norm = value / 10
        color = to_colors([norm], vmin=vmin, vmax=vmax, cmap=cmap)[0]
        artist = ax.plot(
            norm,
            norm,
            marker=n_pointed_star(norms[0](value), 1 - norm, norm**2),
            markersize=30,
            color=color,
        )
        artists.append(artist)

    # Create a ScalarMappable that spans all scatter plots
    combined_scalar = plt.cm.ScalarMappable(cmap="viridis")
    combined_scalar.set_array([vmin, vmax])

    # Create a colorbar using the combined ScalarMappable
    cbar = plt.colorbar(combined_scalar, cax=ax1, aspect=20 / multiply_x, label="color")
    ax1.set_xlim([0.5 - multiply_x / 2, 0.5 + multiply_x / 2])
    ax1.set_xlim([0.5 - multiply_x / 2, 0.5 + multiply_x / 2])

    ax1.yaxis.set_ticks_position("left")
    ax1.yaxis.set_label_position("left")
    vmin, vmax = cbar.norm.vmin, cbar.norm.vmax

    # ticks = cbar.get_ticks()
    # for i, v_color in enumerate(ticks):

    #     print(v_color)
    #     v_marker = v_size = v_color
    #     color = to_colors([v_color], vmin=0, vmax=1, cmap=cmap)[0]
    #     # ax1.plot(0.5, v_color, marker=n_pointed_star(v_marker, v_marker, v_marker), markersize=marker_size(v_color), color=color)
    #     ax2.plot(0.5, v_color, marker=n_pointed_star(v_marker, v_marker, v_marker), markersize=marker_size(v_color), color="grey", fillstyle="none", transform=)

    ax2 = ax1.twinx()

    ax2.set_ylabel("marker size")
    ax2.set_ylim([marker_min, marker_max])
    ax2.yaxis.set_ticks_position("right")
    ax2.yaxis.set_label_position("right")
    ax2.set_position(ax1.get_position())
    for loc in ax1.yaxis.get_ticklocs():
        x, y = 0.5, loc
        transformed_position = ax1.transData.transform((0.5, y))
        x2, y2 = ax2.transData.inverted().transform(transformed_position)
        ax1.plot(
            x,
            y,
            marker=n_pointed_star(norms[0](y2), 1, 1),
            markersize=30,
            color="grey",
            fillstyle="none",
        )

    _ = plt.show()
