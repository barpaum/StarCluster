from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class ElasticIPSetup(ClusterSetup):

    def __init__(self,elasticip):
        self.elasticip = elasticip
        log.debug('elasticip = %s' % elasticip)

    def run(self, nodes, master, user, user_shell, volumes):

        master.ec2.conn.associate_address(master.instance.id,self.elasticip)
