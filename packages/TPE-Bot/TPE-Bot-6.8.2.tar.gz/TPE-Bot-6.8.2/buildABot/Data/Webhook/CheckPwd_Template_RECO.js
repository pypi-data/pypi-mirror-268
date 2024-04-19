function checkPwd(agent){
    const hash = crypto.createHash('sha224');
    const string = agent.parameters.loginID;
    const hashedString = hash.update(string, 'utf-8');
    const gen_hash = hashedString.digest('hex');

    var id;
    var ref = admin.database().ref("ID");
    ref.orderByValue().equalTo(gen_hash).on("child_added", function(snapshot){
      id = snapshot.key;
    });
    
    return admin.database().ref().once("value").then(function(snapshot) {

        var password = snapshot.child("/PWD/" + id + "/password").val();
        const pwd = agent.parameters.pwd;
        const gen_Pwdhash = bcrypt.hashSync(pwd, 10);

        const payload = {
            "richContent": [
              [
                {
                  "text": "Available Assignment Recommended Menu:"
                },
                {
                  "type": "chips",
                  "options": [ LISTOFASSIGNMENTS_CHIPS ]
                }
              ]
            ]
        };

        const payloadTele = {
        "telegram": {
        "text": "Available Assignment Recommended Menu:",
        "reply_markup": {
            "keyboard": [ LISTOFASSIGNMENTS_TELE]
        }
        }
        };

        if(password == null){
            admin.database().ref("/PWD/" + id).set({password: gen_Pwdhash});
            agent.add("🔑 Password Saved");
            agent.add(new Payload(agent.UNSPECIFIED, payload, { rawPayload: true, sendAsMessage: true })); 
            agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true })); 
        }

        else{
          if(bcrypt.compareSync(pwd, password) == true){
            agent.add("✔️ Verification Successful.");
            agent.add(new Payload(agent.UNSPECIFIED, payload, { rawPayload: true, sendAsMessage: true })); 
            agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true })); 
          }
          else{
            agent.add("Hmm.. Seems like it's a wrong password, please try again:");
            checkPwd(agent);
          }
        }
    });
  }