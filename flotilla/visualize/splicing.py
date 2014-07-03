def lavalamp(psi, color=None, jitter=None, title='', ax=None):
    """Make a 'lavalamp' scatter plot of many splicing events

    Useful for visualizing many splicing events at once.

    Parameters
    ----------
    TODO.md: (n_events, n_samples).transpose()
    data : array
        A (n_events, n_samples) matrix either as a numpy array or as a pandas
        DataFrame

    color : matplotlib color
        Color of the scatterplot. Defaults to a dark teal

    title : str
        Title of the plot. Default ''

    ax : matplotlib.Axes object
        The axes to plot on. If not provided, will be created


    Returns
    -------
    fig : matplotlib.Figure
        A figure object for saving.
    """
    from .computation import get_switchy_score_order
    import matplotlib.pyplot as plt


    if ax is None:
        fig, ax = plt.subplots(figsize=(16,4))
    else:
        fig = plt.gcf()
    nrow, ncol = psi.shape
    x = np.vstack(np.arange(nrow) for _ in range(ncol))

    color = '#FFFFFF' if color is None else color

    try:
        # This is a pandas Dataframe
        y = psi.values
    except AttributeError:
        # This is a numpy array
        y = psi

    if jitter is None:
        jitter = np.zeros(len(color))
    else:
        assert np.all(np.abs(jitter) < 1)
        assert np.min(jitter) > -.0000000001

    order = get_switchy_score_order(y.T)
    print order.shape
    y = y[:, order]
    assert type(color) == pd.Series
    # Add one so the last value is actually included instead of cut off
    xmax = x.max() + 1
    x_jitter = np.apply_along_axis(lambda r: r+jitter, 0, x)

    for co, ji, xx, yy in zip(color, jitter, x_jitter, y.T):
        ax.scatter(xx, yy, color=co, alpha=0.5, edgecolor='#262626', linewidth=0.1)
    seaborn.despine()
    ax.set_ylabel('$\Psi$')
    ax.set_xlabel('{} splicing events'.format(nrow))
    ax.set_xticks([])

    ax.set_xlim(0, xmax)
    ax.set_ylim(0, 1)
    ax.set_title(title)

    # Return the figure for saving
    # return fig



from .computation import Predictor
import itertools