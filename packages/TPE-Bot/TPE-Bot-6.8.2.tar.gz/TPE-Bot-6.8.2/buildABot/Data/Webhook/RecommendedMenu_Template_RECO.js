function recommendedMenu (agent){ // ASSIGNMENT NUM MENU HERE //
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
      var name = snapshot.child("/NAME/"+id).val();
      SNAPSHOTHERE // SNAP SHOT 
      // ASSIGNMENT GRADE HERE //
      var flaw = 0;  
      var comment = " ";
      HIGHLIGHTHERE //HIGHLIGHT

      const payloadAndCase = {
        "richContent": [
            [
                {
                    "options": [
                      {
                        "text": "🔎 Learn & Explore"
                      },
                      {
                        "text": "🖋 Results & Recommendation"
                      }
                    ],
                    "type": "chips"
                }
            ]
        ]
        };

        const payloadTele = {
          "telegram": {
          "text": "🗃 No suggested menu in your record, please access other menu for learning... 👇",
          "reply_markup": {
            "keyboard": [
              [
                {
                  "text": "🔎 Learn & Explore",
                  "callback_data": "Learn & Explore"
                },
                {
                  "text": "🖋 Results & Recommendation",
                  "callback_data": "Results & Recommendation"
                }
              ]
            ]
          }
        }
        };
        
        var textReply = "🗃 No suggested menu in your record, please access other menu for learning... 👇";
        // NULL LOOP HERE //
        if(criteria1 == null NULLHERE ){  agent.add(new Payload(agent.UNSPECIFIED, payloadAndCase, { rawPayload: true, sendAsMessage: true })); agent.add(textReply);}
        if(criteria1 == null NULLHERE ){  agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true }));}

        else{
            IFLOOPHERE  // IF LOOP HERE //          
            agent.add('Hi ' + name + ' ! \n ASSIGNMENTGRADEHERE ' + '\n' + 'Grade :	' + grade + '\n'); // REPORT CARD HERE //

            if (flaw == 0) {comment="🎉 Congratulations, You did well for your test! Feel free to ask me anything about the subject...";}
            if (grade == 'F'){comment = "It seems that you did not do well for the areas highlighted below, perhaps you would like to review them again. 📑 \n Keep on fighting and try harder for the next assessment! 💪";}
            if (flaw != 0 && grade != 'F') {comment = "It seems that you did not do well for the topics highlighted below, prehaps you would like to focus on that. 📑";}

            const payloadTele1 = {
              "telegram": {
              "text": "You can explore the menu too! 📂",
              "reply_markup": {
                "keyboard": [[{"text": "🔎 Learn & Explore","callback_data": "Learn & Explore"},{"text": "🖋 Results & Recommendation","callback_data": "Results & Recommendation"}]]
              }
            }
            };

            const payload = {
                "richContent": [
                [
                    {
                    "options": CHIPSPAYLOADHERE ,
                    "type": "chips"
                    }
                ]
                ]
            };

            const payloadTele2 = {
                "telegram": {
                "text": "📂 Pick a topic:",
                "reply_markup": {
                "keyboard": [ TELEPAYLOADHERE ]
                }
            }
            };

          agent.add(comment);
          var textReply2 = "You can explore the menu too! 📂";
          if (flaw == 0) { agent.add(new Payload(agent.UNSPECIFIED, payloadAndCase, { rawPayload: true, sendAsMessage: true })); agent.add(textReply2);}
          if (flaw == 0) { agent.add(new Payload(agent.TELEGRAM, payloadTele1, { rawPayload: true, sendAsMessage: true }));}

          if (flaw != 0) { agent.add(new Payload(agent.UNSPECIFIED, payload, { rawPayload: true, sendAsMessage: true })); }   
          if (flaw != 0) { agent.add(new Payload(agent.TELEGRAM, payloadTele2, { rawPayload: true, sendAsMessage: true })); }        
        }
    });
  }


