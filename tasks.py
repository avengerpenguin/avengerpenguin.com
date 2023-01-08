import voltaire
from invoke import task

namespace = voltaire.site()


@task
def radar(c):
    c.run("node radar.js >extra/radar.json")


namespace.add_task(radar)
namespace.task_with_config("build")[0].pre.append(radar)
namespace.task_with_config("publish")[0].pre.append(radar)
