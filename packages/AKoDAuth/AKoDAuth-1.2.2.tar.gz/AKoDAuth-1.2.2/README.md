![Banner](https://media.discordapp.net/attachments/1092315227057561630/1221146760949272596/actkeys.png?ex=662d340b&is=661abf0b&hm=cb4a68ed29aeb1c89ab073ac36c38fc993c18e3904bc7ab8082af07b4045c945&=&format=webp&quality=lossless&width=960&height=121)
<div align="center">
    </a>
    <br />
    
   [tagoWorks](https://tago.works/) - [AKoD](https://github.com/tagoworks/akod)
   

  Activating Keys on Discord Validating Package is coded to simplify the process of checking keys in your Python projects. Instead of taking up extra lines it handling decryption and key checking, AKoDAuth provides simple functions. You can use the validate function, passing in your email and key variables. AKoDAuth handles all the decryption and checking behind the scenes, allowing you to focus on your main code. For example, you can use `akodauth.isValid(username, password)` to quickly login as long as you have the activation key file set somewhere else, without worrying about additional validation process. To use AKoDAuth in your code and key your code please visit https://github.com/t-a-g-o/akod. View AKoDAuth's PyPi page at https://pypi.org/project/akodauth

</div>

# How to use AKoDAuth

1. Install AKoDAuth

   ```sh
   pip install AKoDAuth
   ```

2. Import & Set AKoD

   ```py
   import AKoDAuth
   ```

   * To set your private key use `AKoDAuth.privatekey('hehSUUXf3m33ns9Hwenj')`
   * To set your authentication webserver link use `AKoDAuth.publicserverkey('jweikAAAA-jemef-efj-_eneiebeufu_38h')`

3. Implement a way to get user input the activation key, then username and login

4. Check if the account and key is valid using AKoDAuth.isValid()
   ```py
   AKoDAuth.setActivationKey('ABCD-1234-ABCD-1234')
   if AKoDAuth.isValid(username, password) == False:
      print("Invalid login!")
      exit
   else:
      # Run your main code here
   ```
