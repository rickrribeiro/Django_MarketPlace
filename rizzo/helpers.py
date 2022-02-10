import uuid

def get_file_path(_instance, filename):
    # ext = filename.split(".")[-1]
    # filename = uuid.uuid4()+"."+ext
    return filename

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])