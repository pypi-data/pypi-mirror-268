# Author: Scott Woods <scott.18.ansar@gmail.com.com>
# MIT License
#
# Copyright (c) 2017-2023 Scott Woods
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Tools and runtime for asynchronous programming.

Repo: git@github.com:mr-ansar/ansar-connect.git
Branch: main
Commit: cf2f9b8e4dded23004c811ba67d180c74ebd6011
Version: 0.1.168 (2024-04-16@01:33:41+NZST)
"""

from ansar.create import *

#bind = bind_any
#create = create_object

from .socketry import HostPort, LocalPort
from .socketry import ScopeOfIP, local_private_public
from .socketry import Blob, CreateFrame
from .socketry import Listening, NotListening, Accepted, NotAccepted, StopListening
from .socketry import Connected, NotConnected
from .socketry import Close, Closed, Abandoned
from .socketry import TlsServer, TlsClient
from .transporting import listen, connect, stop_listen

from .plumbing import RETRY_LOCAL, RETRY_PRIVATE, RETRY_PUBLIC
from .plumbing import ip_retry

from .directory_if import ScopeOfService
from .directory_if import Published, NotPublished, Subscribed
from .directory_if import Available, NotAvailable, Delivered, NotDelivered
from .directory_if import Clear, Cleared, Dropped
from .directory_if import NetworkEnquiry, NetworkConnect, DirectoryScope, DirectoryAncestry

from .directory import ServiceDirectory
from .directory import RouteByRelay, InboundByRelay, OpenLoop, CloseLoop
from .directory import publish, subscribe
from .directory import clear, retract
from .directory import key_service

from .networking_if import UseAddress, NoAddress, GlareTimer
from .networking import ConnectToAddress, ListenAtAddress
from .networking import SubscribeToListing, PublishAListing, SubscribeToSearch
from .grouping import GroupTable, GroupUpdate, AddressGroup, GroupTimer, GroupObject

from .node import NodeSettings, node_settings
from .node import node_passing, sub_node_passing
from .node import create_node, NodeProperties

from .moving import overlay, mirror

from .wan import CONTACT_TYPE, CONTACT_DEVICE
from .wan import EmailAddress, PhoneNumber
