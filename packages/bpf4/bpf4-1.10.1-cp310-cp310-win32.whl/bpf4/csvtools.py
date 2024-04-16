from __future__ import absolute_import as _absimport, division as _division
import csv as _csv
import os as _os
from fractions import Fraction as _Fraction
from collections import namedtuple as _namedtuple


def _could_be_number(s, accept_fractions=False):
    try:
        n = eval(s)
        return isinstance(n, _Number)
    except:
        return False

def _as_number_if_possible(s, accept_fractions=True):
    """try to convert 's' to a number if it is possible"""
    if accept_fractions:
        if "/" in s:
            try:
                n = _Fraction("/".join(n.strip() for n in s.split("/")))
                return n
            except:
                return s
    try:
        n = int(s)
        return n
    except ValueError:
        try:
            n = float(s)
            return n
        except ValueError:
            s
    return s

def replace_non_alfa(s):
    TRANSLATION_STRING = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'__x+,__/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
    return s.translate(TRANSLATION_STRING, '[]#:')

def _normalize_column_name(name):
    name = replace_non_alfa(name)
    if name and name[0] in '0123456789':
        name = 'n' + name
    name = name.strip().rstrip('_')
    return name if name else 'untitled'

def _treat_duplicates(columns):
    names = {}
    new_names = []
    for column in columns:
        if not column in names:
            names[column] = 1
            new_name = column
        else:
            n = names[column]
            n += 1
            names[column] = n
            new_name = "%s_%d" % (column, n)
        new_names.append(new_name)
    return new_names

def readcsv_numpy(csvfile):
    """
    Read CSV into a numpy array
    """
    import numpy
    return numpy.genfromtxt(csvfile, names=True, delimiter=',')

def readcsv(csvfile, rowname=None, transform_numbers=True, astuple=False, prefer_fractions=True, dialect='excel'):
    """
    read a CSV file into a namedtuple
    
    if the first collumn is all text: assume these are the column names
    mode: in some cases you might need to set mode='U' when reading
    files generated by excel in windows

    rowname: override the row name specified in the CSV file (if any)
    transform_numbers: convert strings to numbers if they can be converted
    prefer_fractions: the normal behaviour to treat strings like 3/4 is to treat
                      them as dates. If this is True, fractions will be prefered
    astuple: do not use namedtuples, use normal tuples instead
    """
    assert dialect in _csv.list_dialects()
    mode = "U"
    f = open(csvfile, mode)
    r = _csv.reader(f, dialect=dialect)
    try:
        firstrow = next(r)
    except:
        mode = mode + 'U'
        f = open(csvfile, mode + 'U')
        r = _csv.reader(f, dialect=dialect)
        first_row = next(r)
    attributes = {}
    if firstrow[0].startswith('#'):
        # the first row contains attributes
        f.close()
        f = open(csvfile, mode)
        attribute_line = f.readline()
        attrs = attribute_line[1:].split()
        for attr in attrs:
            key, value = attr.split(':')
            attributes[key] = value
        r = _csv.reader(f, dialect=dialect)
        firstrow = next(r)
    else:
        attrs = None
    if all(not _could_be_number(x) for x in firstrow) or first_row[0].startswith('#'):
        columns = firstrow
    else:
        raise TypeError("""
            Number-like cells found in the first-row. cannot assume column names
            To load simple data you dont need this utility so use normal csv module
            """)
    normalized_columns = [_normalize_column_name(col) for col in columns]
    columns = _treat_duplicates(normalized_columns)
    if attributes:
        a_rowname = attributes.get('rowname')
        rowname = rowname if rowname is not None else a_rowname
    rowname = rowname if rowname is not None else 'Row'
    Row = _namedtuple(rowname, ' '.join(columns))
    numcolumns = len(columns)
    rows = []
    for row in r:
        if transform_numbers:
            row = [_as_number_if_possible(cell, accept_fractions=prefer_fractions) for cell in row]
        if not astuple:
            if len(row) == numcolumns:
                rows.append(Row(*row))
            else:
                row.extend([''] * (numcolumns - len(row)))
                row = row[:numcolumns]
                rows.append(Row(*row))
        else:
            rows.append(row)
    return rows

def read(*args, **kws):
    import warnings
    warnings.warn("This function has been renamed to readcsv")
    return readcsv(*args, **kws)

def readcsv_tabs(csvfile, transform_numbers=True, as_tuple=False):
    """
    read a csv file which uses tabs instead of commas as column-divider
    """
    return read(csvfile, transform_numbers=transform_numbers, as_tuple=as_tuple, dialect='excel-tab')

def writecsv(namedtuples, outfile, column_names=None, write_row_name=False):
    """
    write a sequence of named tuples to outfile as CSV

    alternatively, you can also specify the column_names. in this case it
    is not necessary for the tuples to be be namedtuples
    """
    firstrow = namedtuples[0]
    isnamedtuple = hasattr(firstrow, '_fields')
    if isnamedtuple:
        column_names = firstrow._fields
    outfile = _os.path.splitext(outfile)[0] + '.csv'
    def parse_fractions(row):
        def parse_fraction(cell):
            if isinstance(cell, Fraction):
                return "0 %s" % str(cell)
            elif isinstance(cell, str) and "/" in cell:
                return '"%s"' % str(cell)
            return cell
        row = list(map(parse_fraction, row))
        return row
    f = open(outfile, 'wb')
    f_write = f.write
    w = _csv.writer(f)
    if isnamedtuple and write_row_name:
        try:
            rowname = firstrow.__doc__.split('(')[0] # <-- this is a hack! where is the name of a namedtuple??
        except AttributeError:  # maybe not a namedtuple in the end
            rowname = firstrow.__class__.__name__
        line = "# rowname:%s\n" % rowname
        f_write(line)
    if column_names:
        w.writerow(column_names)
    for row in namedtuples:
        try:
            w.writerow(row)
        except:
            w.writerow(tuple(row))
    f.close()

def _to_number(x, accept_fractions=True):
    if _could_be_number(x, accept_fractions=accept_fractions):
        if '.' in x or x in ('nan', 'inf', '-inf'):
            return float(x)
        else:
            try:
                return int(x)
            except:
                try:
                    return _Fraction(x)
                except:
                    return x
    else:
        return x

# class NamedTuples(list):
#     def __init__(self, column_names, row_name='_'):
#         self.factory = _namedtuple(row_name, column_names)
#         if isinstance(column_names, basestring):
#             column_names = [name.strip() for name in (column_names.split(',') if ',' in column_names else column_names.split())]
#         self.column_names = column_names
#     def append(self, *args, **keys):
#         list.append(self, self.factory(*args, **keys))
#     def writecsv(self, outfile):
#         writecsv(self, outfile, self.column_names)
#     @classmethod
#     def readcsv(self, csvfile):
#         rows = read(csvfile)
#         row_name = '_'
#         column_names = ' '.join(rows[0]._fields)
#         out = NamedTuples(row_name, column_names)
#         out.extend(rows)
#         return out

