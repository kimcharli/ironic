# Copyright 2016 Intel Corporation
# Copyright 2013,2014 Cray Inc
#
# Authors: David Hewson <dhewson@cray.com>
#          Stig Telfer <stelfer@cray.com>
#          Mark Goddard <mgoddard@cray.com>
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from ironic.common.i18n import _

opts = [
    cfg.IntOpt('power_timeout',
               default=10,
               help=_('Seconds to wait for power action to be completed')),
    # NOTE(yuriyz): some of SNMP-enabled hardware have own options for pause
    # between off and on. This option guarantees minimal value.
    cfg.IntOpt('reboot_delay',
               default=0,
               min=0,
               help=_('Time (in seconds) to sleep between when rebooting '
                      '(powering off and on again)'))
]


def register_opts(conf):
    conf.register_opts(opts, group='snmp')
