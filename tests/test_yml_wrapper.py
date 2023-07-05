import os
import inspect
import yaml
from jon.jon_wrapper import JONFactory

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def test_simple_manifest():
    with open(script_dir + '/k8s_simple_manifest.yml', 'r') as stream:
        try:
            d = yaml.safe_load(stream)
            json_obj2 = JONFactory.wrap(d)

            assert json_obj2.kind == 'Deployment'
            assert json_obj2.metadata.labels.app == 'consumer'
            assert json_obj2.spec.template.spec.containers[0].image == 'emmerson/cdi-rabbit-consumer:1.1.0'

        except yaml.YAMLError as e:
            print(e)


def test_multiple_manifest():
    with open(script_dir + '/k8s_manifests.yml', 'r') as stream:
        try:
            docs = yaml.safe_load_all(stream)
            all = [JONFactory.wrap(doc) for doc in docs]
            assert len(all) == 10
            assert all[0].metadata.name == 'consumer-configmap'
            assert all[0].data.RABBIT_HOST == 'rabbitmq'
            assert all[1].metadata.name == 'producer-configmap'

            assert all[2].kind == 'Service'
            assert all[2].metadata.labels.app == 'rabbitmq'
        except yaml.YAMLError as e:
            print(e)

