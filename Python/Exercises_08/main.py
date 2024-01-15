from devices import Firewall, Switch, LoadBalancer

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switch instance
switch1 = Switch("switch12")
# Configure it
switch1.configure_switch()
switch1.calculate_crc("dummy data")

# Create a load balancer instance
load_balancer1 = LoadBalancer("load_balancer33")
# Configure it
load_balancer1.configure_load_balancer()
load_balancer1.calculate_crc("dummy data")
