ansible-playbook ansible/configure-host.yml -e "student_username=iniles"
ansible-playbook ansible/deploy-website-staging.yml
ansible-playbook ansible/deploy-website-production.yml
