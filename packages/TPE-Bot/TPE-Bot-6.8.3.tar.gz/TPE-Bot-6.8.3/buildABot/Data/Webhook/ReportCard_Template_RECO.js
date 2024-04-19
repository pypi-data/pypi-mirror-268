  function recommendedMenu(agent){
    const loginID = agent.parameters.loginID;

    if (loginID){
      const hash = crypto.createHash('sha224');
      const hashedString = hash.update(loginID, 'utf-8');
      const gen_hash = hashedString.digest('hex');
      const ref = admin.database().ref("ID");

      var id;
      ref.orderByValue().equalTo(gen_hash).on("child_added", function(snapshot){
          id = snapshot.key;
      });

      return admin.database().ref().once("value").then(function(snapshot) {
        var name = snapshot.child("/NAME/"+id).val();
        var feedback = snapshot.child("/#AssignmentFeedback/"+id).val();
        SNAPSHOTHERE
        // ASSIGNMENT GRADE HERE //

        #ASSIGNMENTREPORTCARD(agent, name, grade, feedback, CRITERIASHERE);
      });
    } 

    if(request.body.originalDetectIntentRequest.payload.data){
      const username = request.body.originalDetectIntentRequest.payload.data.from.username;
      const chat = request.body.originalDetectIntentRequest.payload.data.chat.type;
      const ref = admin.database().ref("Telegram ID");

      var teleID;
      ref.orderByValue().equalTo(username).on("child_added", function(snapshot){
        teleID = snapshot.key;
      });
      
      if(chat != 'private'){
        agent.add(new Text('Please check you report card in a private chat with me instead 🤗.'));
      }

      else{
        return admin.database().ref().once("value").then(function(snapshot) {
          var name = snapshot.child("/NAME/"+teleID).val();
          var feedback = snapshot.child("/#AssignmentFeedback/"+teleID).val();
          // TELE SNAPSHOT HERE //
          // TELEASSIGNMENT GRADE HERE //

          #ASSIGNMENTREPORTCARD(agent, name, grade, feedback, CRITERIASHERE);
        });
      }
    }

    
  }

  
  function #ASSIGNMENTREPORTCARD(agent, name, grade, feedback, CRITERIASHERE){
    var flaw = 0; 
    HIGHLIGHTHERE
    if (criteria1 ==null NULLHERE){ //
      const buttonDefPayload = {
          "richContent": [
              [
                {
                  "options": [
                    {
                      "text": "See Topics"
                    }
                  ],
                  "type": "chips"
                }
            ]
          ]
      };

      const payloadTele = {
        "telegram": {
        "text": "You can explore the menu! 📂",
        "reply_markup": {
          "keyboard": [[{"text": "🔎 Learn & Explore","callback_data": "Learn & Explore"},{"text": "🖋 Results & Recommendation","callback_data": "Results & Recommendation"}]]
        }
      }
      };
      
      agent.add("No report card available...");
      agent.add(new Payload(agent.UNSPECIFIED, buttonDefPayload, { rawPayload: true, sendAsMessage: true }));
      agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true }));
    }

    else{
      // IF LOOP //
      IFLOOPHERE
      const buttonPayload = {
        "richContent": [
          [
            {
              "type": "description",
              "title": '-- '+ name + "ASSIGNMENTGRADEHERE",
              "text": [
                'Grade : ' + grade ,
                feedback
              ]
            },
            {
                "options": CHIPSPAYLOADHERE,
                "type": "chips"
            }
          ]
        ]
      };

      const payloadTele = {
        "telegram": { 
        "text": '-- '+ name + 'ASSIGNMENTGRADEHERE \n Grade : ' + grade + '\n\n' + feedback,
        "reply_markup": {
          "keyboard": [ TELEPAYLOADHERE ]
          }
        }
      };
      
      agent.add(new Payload(agent.UNSPECIFIED, buttonPayload, { rawPayload: true, sendAsMessage: true }));
      agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true }));
    }
  }