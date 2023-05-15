from fabric import task, Config
from datetime import datetime

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, None otherwise.
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        c.local("mkdir -p versions")
        c.local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None
