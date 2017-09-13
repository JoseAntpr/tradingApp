API_VERSION = "2"

Vagrant.configure(API_VERSION) do |config|
    config.vm.box = "geerlingguy/ubuntu1604"

    config.vm.network "forwarded_port", guest: 80, host: 8000
    config.vm.network "private_network", ip:"192.168.33.10" 
    
    # Acceso SSH y sincroniczar nuestro directorio
    config.ssh.forward_agent = true
    config.vm.synced_folder "./", "/var/www/tradingApp"
    
    config.ssh.forward_agent = true

    config.vm.provision :ansible do |ansible|
        ansible.playbook = "provision/vagrant.yml"
    end
end




