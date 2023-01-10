import voltaire
from invoke import task

namespace = voltaire.site()


@task
def radar(c, output_path="output/radar"):
    c.run("node radar.js >extra/radar.json")
    c.run(f"mkdir -p {output_path}")
    print(output_path)
    c.run(
        f"docker build -t radar -f Dockerfile.radar --output type=local,dest={output_path} ."
    )
    c.run(f"tree {output_path}/..")


@task
def radar_publish(c):
    radar(c, output_path="dist/radar")


namespace.add_task(radar)
namespace.task_with_config("build")[0].post.append(radar)

namespace.add_task(radar_publish)
namespace.task_with_config("publish")[0].post.append(radar_publish)
