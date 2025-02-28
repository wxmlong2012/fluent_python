import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 400)
np.set_printoptions(linewidth=400)

data = """
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
|       CVE        | SEVERITY | CVSS |    PACKAGE    |        VERSION         |               STATUS                |  PUBLISHED  | DISCOVERED |                    DESCRIPTION                     |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2019-12900   | critical | 9.80 | python        | 3.9.7                  | fixed in 3.10.3, 3.9.11, 3.8.13,... | > 3 years   | < 1 hour   | BZ2_decompress in decompress.c in bzip2 through    |
|                  |          |      |               |                        | > 3 years ago                       |             |            | 1.0.6 has an out-of-bounds write when there are    |
|                  |          |      |               |                        |                                     |             |            | many selectors.                                    |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2016-10164   | critical | 9.80 | libxpm        | 1:3.5.12-1.1~deb11u1   | fixed in 1:3.5.12-1                 | > 6 years   | < 1 hour   | Multiple integer overflows in libXpm before        |
|                  |          |      |               |                        | > 6 years ago                       |             |            | 3.5.12, when a program requests parsing XPM        |
|                  |          |      |               |                        |                                     |             |            | extensions on a 64-bit platform, allow remote      |
|                  |          |      |               |                        |                                     |             |            | attackers to cau...                                |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| PRISMA-2022-0168 | high     | 7.80 | pip           | 23.1.2                 | open                                | > 1 years   | < 1 hour   | An issue was discovered in pip (all versions)      |
|                  |          |      |               |                        |                                     |             |            | because it installs the version with the highest   |
|                  |          |      |               |                        |                                     |             |            | version number, even if the user had intended to   |
|                  |          |      |               |                        |                                     |             |            | obtain...                                          |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2022-42919   | high     | 7.80 | python        | 3.9.7                  | fixed in 3.10.9, 3.9.16             | > 6 months  | < 1 hour   | Python 3.9.x before 3.9.16 and 3.10.x before       |
|                  |          |      |               |                        | > 6 months ago                      |             |            | 3.10.9 on Linux allows local privilege escalation  |
|                  |          |      |               |                        |                                     |             |            | in a non-default configuration. The Python         |
|                  |          |      |               |                        |                                     |             |            | multiprocess...                                    |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2015-20107   | high     | 7.60 | python        | 3.9.7                  | fixed in 3.10.8                     | > 1 years   | < 1 hour   | In Python (aka CPython) up to 3.10.8, the mailcap  |
|                  |          |      |               |                        | > 1 years ago                       |             |            | module does not add escape characters into         |
|                  |          |      |               |                        |                                     |             |            | commands discovered in the system mailcap file.    |
|                  |          |      |               |                        |                                     |             |            | This may ...                                       |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2023-24329   | high     | 7.50 | python        | 3.9.7                  | fixed in 3.11                       | > 3 months  | < 1 hour   | An issue in the urllib.parse component of          |
|                  |          |      |               |                        | 85 days ago                         |             |            | Python before v3.11 allows attackers to bypass     |
|                  |          |      |               |                        |                                     |             |            | blocklisting methods by supplying a URL that       |
|                  |          |      |               |                        |                                     |             |            | starts with blan...                                |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2022-45061   | high     | 7.50 | python        | 3.9.7                  | fixed in 3.11.1, 3.10.9, 3.9.16,... | > 6 months  | < 1 hour   | An issue was discovered in Python before 3.11.1.   |
|                  |          |      |               |                        | > 5 months ago                      |             |            | An unnecessary quadratic algorithm exists in one   |
|                  |          |      |               |                        |                                     |             |            | path when processing some inputs to the IDNA (RFC  |
|                  |          |      |               |                        |                                     |             |            | 34...                                              |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2022-40898   | high     | 7.50 | wheel         | 0.37.0                 | fixed in 0.38.1                     | > 5 months  | < 1 hour   | An issue discovered in Python Packaging Authority  |
|                  |          |      |               |                        | > 4 months ago                      |             |            | (PyPA) Wheel 0.37.1 and earlier allows remote      |
|                  |          |      |               |                        |                                     |             |            | attackers to cause a denial of service via         |
|                  |          |      |               |                        |                                     |             |            | attacker co...                                     |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2020-10735   | high     | 7.50 | python        | 3.9.7                  | fixed in 3.10.7, 3.9.14, 3.8.14,... | > 8 months  | < 1 hour   | A flaw was found in python. In algorithms with     |
|                  |          |      |               |                        | > 5 months ago                      |             |            | quadratic time complexity using non-binary bases,  |
|                  |          |      |               |                        |                                     |             |            | when using int(\"text\"), a system could take 50ms |
|                  |          |      |               |                        |                                     |             |            | to...                                              |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
| CVE-2018-25032   | high     | 7.50 | python        | 3.9.7                  | fixed in 1.2.12                     | > 1 years   | < 1 hour   | zlib before 1.2.12 allows memory corruption when   |
|                  |          |      |               |                        | > 1 years ago                       |             |            | deflating (i.e., when compressing) if the input    |
|                  |          |      |               |                        |                                     |             |            | has many distant matches.                          |
+------------------+----------+------+---------------+------------------------+-------------------------------------+-------------+------------+----------------------------------------------------+
"""


def wrap_output(data):
    # Remove leading/trailing whitespaces and split the data into lines
    lines = data.strip().split('\n')

    # Extract header row and content rows
    header = [col.strip() for col in lines[1].split('|')[1:-1]]
    rows = [line.strip().split('|')[1:-1] for line in lines[3:-2]]

    # Remove leading/trailing whitespaces from each cell
    rows = [[col.strip() for col in row] for row in rows]

    # Create a pandas DataFrame
    df = pd.DataFrame(rows, columns=header)

    # Drop None in CVE column
    df = df.dropna(subset=["CVE"])

    # Replace "" with None
    df["CVE"] = df["CVE"].replace("", None)

    # Forward fill the missing values in the 'CVE' column
    df['CVE'].fillna(method='ffill', inplace=True)

    # Combine the text for each column based on group
    grouped_df = df.groupby('CVE').agg(lambda x: ' '.join(x.dropna()))

    # Remove white spaces.
    grouped_df = grouped_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return grouped_df

