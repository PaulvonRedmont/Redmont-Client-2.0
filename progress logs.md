## Attempt #1: Tried using a robotics kit to manually push the “listen” button on Alexa, and had an audio recording on loop.

**Result: Failure.** 

**Reason:** Alexa stops responding to all commands, both verbal and physical after approximately 100 inputs, both verbal and physical. To fix this, one must restart the device, by unplugging and replugging the Echo Dot.

## Attempt #2: Tried using a robotics kit to type in commands in the Alexa App on an iPhone.

**Result: Failure.**

**Reason:** Alexa has varied response times, and this “macro” had no way of knowing what the heck Alexa was saying.

## Attempt #3: Tries using a robotics kit to type in commands in the Alexa App on an iPhone, as well as using OCR (Optical Character Recognition) to try and detect the words on the phone.

**Result: Failure.**

**Reason:** OCR apparently does not entirely work for images that glow (namely, an iPhone. Furthermore, this method would require a user to keep their phone on for massive amounts of time, and not be able to use it while the macro was running.

## Attempt #4: Tried using a mobile app to bot the Alexa app on an iPhone.

**Result: Failure.**

**Reason:** This method would require a user to keep their phone on for massive amounts of time, and not be able to use it while the macro was running. Also, mobile development is a P A I N.

## Attempt #5: Tried using MacOS’s iPhone simulator, which would allow me to create a macro using Python or Pyautogui to bot the Alexa App via a PC.

**Result: Failure.**

**Reason:** 1) using a Virtual Box to run the MacOS iPhone Simulator is potentially illegal and 2) rather difficult.

## Attempt #6: Tried using the BlueStacks software to use the mobile version of the Alexa App on the PC.

**Result: Failure.**

**Reason:** 1) BlueStacks refused to properly run the Alexa App, and 2) BlueStacks is probably a virus, and even if it isn’t, it’s one VERY poorly designed program.

## Attempt #7: Tried to use Wireshark or some other packet sniffer to see if I could spoof the Alexa API.

**Result: Failure.**

**Reason:** 1) it might have been illegal, 2) it was very hard to spoof the authentication tokens and 3) it took forever.

## Attempt #8: Tried to use Virtual Audio Cables and the PC Alexa App to bot it using audio recordings and the pocketsphinx library.

**Result: Success.**

**NOTE:** While attempt #8 did technically work, the pocketsphinx library was, frankly, awful. As knight manager has a significant built-in background noise of combat, the blacksmith, etc. the already buggy pocketsphinx library performed even worse, and was of no help whatsoever. However, it did give some insight into the means by which one might be able to bot the Alexa App, and suggested that the problem here was merely in having a good speech-to-text application.

## Attempt #9: Tried to use Virtual Audio Cables and the PC Alexa App to bot it using audio recordings and the Vosk speech recognition toolkit (vosk-model-en-us-0.42-gigaspeech).

**Result: Success.**

**NOTE:** Attempt #9 was much better than Attempt #8, as the accuracy of the model was approximately 392% higher than pocketsphinx. However, vosk-model-en-us-0.42-gigaspeech did have some flaws, most notably being that it was unable to accurately recognize words when there was background noise in the game. The model did note that it was “Mostly for podcasts, not for telephony.”  I theorize that the issue is with the pre-trained model itself, as it was not meant for intensive background noise audio transcription.

**Addendum:** As of 3/1/23, the Alexa App for the PC is no longer available. Other routes must be evaluated and reconsidered. 

UPDATE (3/16/24): Switched focus to OCR and BlueStacks (which I was able to get working). OCR and basic text searching produces unsatisfactory results. Researching how AI could help isolate text of interest

## Attempt #10 (7/3/24): Going back to Bluestacks with ADB client and increased OCR accuracy.

After a 4-month break from this project, I have made more breakthroughs in the last two days than in the last year. By resetting my PC, and reinstalling Bluestacks (the security of which I have heavily researched), I now have much faster performance in general from this app. Not only this, but I now am using the ADB and ppadb libraries and drivers to create a client to grab screenshots and tap coordinates from the Bluestacks emulator, essentially removing the need for pyautogui, which was incredibly crude and buggy. This means that one can now have access to a full on API for the Bluestacks emulator.In addition, I have been researching different methods by which to increase OCR accuracy in other projects, and now realize that the most computationally efficient manner in which to increase accuracy is to increase image size before running the image through the tesseract models. This allows for at least a 17% increase in accuracy, although I must do some more benchmarking to see if the number is actually a lot higher (just by looking at the results, I personally feel that it is at least 50% more accurate). Things took a radical turn from four months ago, and I fully intend to continue with this project until it reaches completion. The only bits left that really needed to be coded are the UI, logic  and text processing, and logs for the client.
