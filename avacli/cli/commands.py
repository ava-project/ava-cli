
class Commands(object):

    def login(self):
        """
        Generate a Distributed Application Bundle (DAB) from the Compose file.

        Images must have digests stored, which requires interaction with a
        Docker registry. If digests aren't stored for all images, you can fetch
        them with `docker-compose pull` or `docker-compose push`. To push images
        automatically when bundling, pass `--push-images`. Only services with
        a `build` option specified will have their images pushed.

        Usage: login [options]
        """
        print('test')
