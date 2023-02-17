# Solution

## Apache task

1. Have used ansible to perform the task.

### Prerequisites

1. Ansible and goss (to test) are installed

### To Run

```bash
$ cd ansible 
$ ansible-playbook main.yml --ask-become-pass
```

### To Test

```bash
$ cd ansible
$ goss validate
```

## Credit Card Validation task

### To Run

```bash
$ python3 credit_card_validator.py 
Enter Number Of Cards: 6
Enter card 1: 4123456789123456
Valid
Enter card 2: 5123-4567-8912-3456
Valid
Enter card 3: 61234-567-8912-3456
Invalid
Enter card 4: 4123356789123456
Valid
Enter card 5: 5133-3367-8912-3456
Invalid
Enter card 6: 5123 - 3567 - 8912 - 3456
Invalid
```