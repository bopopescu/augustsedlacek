 # coding=utf-8

def format_element(bfo, limit, max_chars,
           highlight='no', escape="3",
           separator="<br/>"):
    """ Prints whole Card File record Heading (Zahlavi).

    @param highlight: if 'yes' highlights words from user search keyword
    @param escape: escaping method (overrides default escape parameter to not escape separators)
    @param separator: a separator between each english abstract
    """
    out = ''

    try:
        escape_mode_int = int(escape)
    except ValueError, e:
        escape_mode_int = 0

    zahlavi = bfo.fields('190%%3', escape=escape_mode_int)
    zahlavi.extend(bfo.fields('190%%a', escape=escape_mode_int))
    zahlavi.extend(bfo.fields('190%%g', escape=escape_mode_int))

    i = 0;
    for x in zahlavi:
        if x != "":
            i = i+1
            if i > 1:
                out += ', '
            out += x

    if out == "":
        out = "[Prázdné záhlaví]" 

    if highlight == 'yes':
        out = bibformat_utils.highlight(out, bfo.search_pattern)

    return out

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
