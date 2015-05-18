# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.keystore.v1 import container
from openstack.keystore.v1 import order
from openstack.keystore.v1 import secret
from openstack import proxy


class Proxy(proxy.BaseProxy):

    def create_container(self, **attrs):
        """Create a new container from attributes

        :param dict attrs: Keyword arguments which will be used to create
               a :class:`~openstack.keystore.v1.container.Container`,
               comprised of the properties on the Container class.

        :returns: The results of container creation
        :rtype: :class:`~openstack.keystore.v1.container.Container`
        """
        return self._create(container.Container, **attrs)

    def delete_container(self, value, ignore_missing=True):
        """Delete a container

        :param value: The value can be either the ID of a container or a
               :class:`~openstack.keystore.v2.container.Container` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the container does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent container.

        :returns: ``None``
        """
        self._delete(container.Container, value, ignore_missing)

    def find_container(self, name_or_id):
        """Find a single container

        :param name_or_id: The name or ID of a container.
        :returns: One :class:`~openstack.compute.v2.container.Container` or
                  None
        """
        return container.Container.find(self.session, name_or_id)

    def get_container(self, value):
        """Get a single container

        :param value: The value can be the ID of a container or a
                      :class:`~openstack.keystore.v1.container.Container`
                      instance.

        :returns: One :class:`~openstack.keystore.v1.container.Container`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(container.Container, value)

    def containers(self):
        """Return a generator of containers

        :returns: A generator of container objects
        :rtype: :class:`~openstack.keystore.v1.container.Container`
        """
        return self._list(container.Container)

    def update_container(self, value, **attrs):
        """Update a container

        :param value: Either the id of a container or a
                      :class:`~openstack.compute.v2.container.Container`
                      instance.
        :attrs kwargs: The attributes to update on the container represented
                       by ``value``.

        :returns: The updated container
        :rtype: :class:`~openstack.compute.v2.container.Container`
        """
        return self._update(container.Container, value, **attrs)

    def create_order(self, **attrs):
        """Create a new order from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.keystore.v1.order.Order`,
                           comprised of the properties on the Order class.

        :returns: The results of order creation
        :rtype: :class:`~openstack.keystore.v1.order.Order`
        """
        return self._create(order.Order, **attrs)

    def delete_order(self, value, ignore_missing=True):
        """Delete an order

        :param value: The value can be either the ID of a order or a
                      :class:`~openstack.keystore.v2.order.Order` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the order does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent order.

        :returns: ``None``
        """
        self._delete(order.Order, value, ignore_missing)

    def find_order(self, name_or_id):
        """Find a single order

        :param name_or_id: The name or ID of a order.
        :returns: One :class:`~openstack.compute.v2.order.Order` or None
        """
        return order.Order.find(self.session, name_or_id)

    def get_order(self, value):
        """Get a single order

        :param value: The value can be the ID of an order or a
                      :class:`~openstack.keystore.v1.order.Order`
                      instance.

        :returns: One :class:`~openstack.keystore.v1.order.Order`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(order.Order, value)

    def orders(self):
        """Return a generator of orders

        :returns: A generator of order objects
        :rtype: :class:`~openstack.keystore.v1.order.Order`
        """
        return self._list(order.Order)

    def update_order(self, value, **attrs):
        """Update a order

        :param value: Either the id of a order or a
                      :class:`~openstack.compute.v2.order.Order` instance.
        :attrs kwargs: The attributes to update on the order represented
                       by ``value``.

        :returns: The updated order
        :rtype: :class:`~openstack.compute.v2.order.Order`
        """
        return self._update(order.Order, value, **attrs)

    def create_secret(self, **attrs):
        """Create a new secret from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.keystore.v1.secret.Secret`,
                           comprised of the properties on the Order class.

        :returns: The results of secret creation
        :rtype: :class:`~openstack.keystore.v1.secret.Secret`
        """
        return self._create(secret.Secret, **attrs)

    def delete_secret(self, value, ignore_missing=True):
        """Delete a secret

        :param value: The value can be either the ID of a secret or a
                      :class:`~openstack.keystore.v2.secret.Secret` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the secret does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent secret.

        :returns: ``None``
        """
        self._delete(secret.Secret, value, ignore_missing)

    def find_secret(self, name_or_id):
        """Find a single secret

        :param name_or_id: The name or ID of a secret.
        :returns: One :class:`~openstack.compute.v2.secret.Secret` or None
        """
        return secret.Secret.find(self.session, name_or_id)

    def get_secret(self, value):
        """Get a single secret

        :param value: The value can be the ID of a secret or a
                      :class:`~openstack.keystore.v1.secret.Secret`
                      instance.

        :returns: One :class:`~openstack.keystore.v1.secret.Secret`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(secret.Secret, value)

    def secrets(self):
        """Return a generator of secrets

        :returns: A generator of secret objects
        :rtype: :class:`~openstack.keystore.v1.secret.Secret`
        """
        return self._list(secret.Secret)

    def update_secret(self, value, **attrs):
        """Update a secret

        :param value: Either the id of a secret or a
                      :class:`~openstack.compute.v2.secret.Secret` instance.
        :attrs kwargs: The attributes to update on the secret represented
                       by ``value``.

        :returns: The updated secret
        :rtype: :class:`~openstack.compute.v2.secret.Secret`
        """
        return self._update(secret.Secret, value, **attrs)
