import os
import sys
import shutil
from flowci import domain, client

def sendReport(path, entryFile):
    if not os.path.exists(path):
        print("'{}' not existed".format(path))
        return

    upload = path
    isZipFile = "false"

    if os.path.isdir(path):
        zipFileName = os.path.basename(path)
        upload = shutil.make_archive(zipFileName, 'zip', path)
        isZipFile = "true"    
        print("zipped.")

    api = client.Client()

    status = api.sendJobReport(
        path=upload, 
        name=domain.JobReportCodeCoverage,
        zipped=isZipFile,
        contentType=domain.ContentTypeHtml,
        entryFile=entryFile
    )

    print("{} report uploaded with status {}".format(path, status))


entryFile = "index.html"
path = sys.argv[1]

if len(sys.argv) == 3:
    entryFile = sys.argv[2]

sendReport(path, entryFile)
