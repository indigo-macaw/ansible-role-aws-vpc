#!/usr/bin/env python


def pcxs_to_routes(pcxs, my_vpc_id):
    routes = []
    for pcx in pcxs['VpcPeeringConnections']:
        their_cidr_block = None
        if my_vpc_id == pcx['AccepterVpcInfo']['VpcId']:
            their_cidr_block = pcx['RequesterVpcInfo']['CidrBlock']
        elif my_vpc_id == pcx['RequesterVpcInfo']['VpcId']:
            their_cidr_block = pcx['AccepterVpcInfo']['CidrBlock']
        if their_cidr_block and \
           pcx['Status']['Code'] == 'active':
            routes.append({"dest": their_cidr_block,
                           "vpc_peering_connection_id":
                               pcx['VpcPeeringConnectionId']})
    return routes


class FilterModule (object):
    def filters(self):
        return {
            "pcxs_to_routes": pcxs_to_routes
        }
