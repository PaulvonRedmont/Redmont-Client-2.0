## Attempt #1: Tried using a robotics kit to manually push the “listen” button on Alexa, and had an audio recording on loop.

**Result: Failure.** 

**Reason:** Alexa stops responding to all commands, both verbal and physical after approximately 100 inputs (both verbal and physical). To fix this, one must restart the device, by unplugging and replugging the Echo Dot, which would be a serious technical challenge of timing and manufactured dexterity.

## Attempt #2: Tried using a robotics kit to type in commands in the Alexa App on an iPhone.

**Result: Failure.**

**Reason:** Alexa has varied response times, and this “macro” had no way of knowing what the heck Alexa was saying.

## Attempt #3: Tries using a robotics kit to type in commands in the Alexa App on an iPhone, as well as using a live webcam and OCR (Optical Character Recognition) to try and detect the words on the phone.

**Result: Failure.**

**Reason:** OCR apparently does not entirely work all that well for images that glow (namely, an iPhone). Furthermore, this method would require a user to keep their phone on for massive amounts of time, and not be able to use it while the macro was running. And if we're literally having to build all these custom scripts for increased image sharpness and quality for OCR, we might as well try and bot it on the software side.

## Attempt #4: Tried using a mobile app to bot the Alexa app on an iPhone.

**Result: Failure.**

**Reason:** This method would require a user to keep their phone on for massive amounts of time, and not be able to use it while the macro was running. Also, mobile development is a P A I N, and I'm not anxious to get into it.

## Attempt #5: Tried using MacOS’s iPhone simulator, which would allow me to create a macro using Python or Pyautogui to bot the Alexa App via a PC.

**Result: Failure.**

**Reason:** 1) using a Virtual Box to run the MacOS iPhone Simulator is potentially illegal and 2) rather difficult, as you have to convert the macos operating system into an image that VB can run.

## Attempt #6: Tried using the BlueStacks software to use the mobile version of the Alexa App on the PC.

**Result: Failure.**

**Reason:** 1) BlueStacks refused to properly run the Alexa App, and 2) BlueStacks is probably a virus, and even if it isn’t, it’s one VERY poorly designed and buggy program.

## Attempt #7: Tried to use Wireshark or some other packet sniffer to see if I could spoof the authentication tokens of my Echo Dot.

**Result: Failure.**

**Reason:** Ok, so this attempt was actually a lot harder than I initially thought. First of all, it turns out that trying to hack your own devices is actually a lot harder than it sounds, even when you literally have full knowledge of the network password, your Amazon login, etc. Second, Amazon basically has airtight encryption and authentication, so I doubt even a cybersecurity professional (which I am most certainly not)  could bypass these safeguards. However, I do think there is a lot to be said for this method, despite its insane difficulty. If I had been able to get this thing to work, I could have botted the Alexa app with a lot more ease than other methods...

## Attempt #8: Tried to use Virtual Audio Cables and the PC Alexa App to bot it using audio recordings and the pocketsphinx library.

**Result: Success.**

**NOTE:** While attempt #8 did technically work, the pocketsphinx library was, frankly, awful. As Knight Manager has a significant built-in background noise of combat, the blacksmith, etc. the already buggy pocketsphinx library performed even worse and was of no help whatsoever. However, it did give some insight into the means by which one might be able to bot the Alexa App and suggested that the problem here was merely in having a good speech-to-text application.

## Attempt #9: Tried to use Virtual Audio Cables and the PC Alexa App to bot it using audio recordings and the Vosk speech recognition toolkit (vosk-model-en-us-0.42-gigaspeech).

**Result: Success.**

**NOTE:** Attempt #9 was much better than Attempt #8, as the accuracy of the model was approximately 392% higher than pocketsphinx. However, vosk-model-en-us-0.42-gigaspeech did have some flaws, most notably being that it was unable to accurately recognize words when there was background noise in the game. The model did note that it was “Mostly for podcasts, not for telephony.”  I theorize that the issue is with the pre-trained model itself, as it was not meant for intensive background noise audio transcription.

**Addendum:** As of 3/1/23, the Alexa App for the PC is no longer available. Other routes must be evaluated and reconsidered. 

UPDATE (3/16/24): Switched focus back to OCR and BlueStacks (which I was able to get working). OCR and basic text searching produces unsatisfactory results. Researching how AI could help isolate text of interest. Perhaps a simple text sorting and parsing algorithm could also do the trick.

## Attempt #10 (7/3/24): Going back to Bluestacks with ADB client and increased OCR accuracy.

**Result: Success, Progress still ongoing.**

After a 4-month break from this project, I have made more breakthroughs in the last two days than in the last year. By resetting my PC, and reinstalling Bluestacks (the security of which I have heavily researched), I now have much faster performance in general from this app. Not only this, but I now am using the ADB and ppadb libraries and drivers to create a client to grab screenshots and tap coordinates from the Bluestacks emulator, essentially removing the need for pyautogui, which was incredibly crude and buggy. This means that one can now have access to a full-on API for the Bluestacks emulator. In addition, I have been researching different methods by which to increase OCR accuracy in other projects, and now realize that the most computationally efficient manner in which to increase accuracy is to increase image size before running the image through the tesseract models. This allows for at least a 17% increase in accuracy, although I must do some more benchmarking to see if the number is actually a lot higher (just by looking at the results, I personally feel that it is at least 50% more accurate). Things took a radical turn from four months ago, and I fully intend to continue with this project until it reaches completion. The only bits left that really needed to be coded are the UI, logic  and text processing, and logs for the client.

# Update 7/10/24: openCV additions

After a week of progress, I believe I have been able to successfully create a fully functional client, capable of screenshotting the emulator, entering and sending messages through the Alexa App, and finding the latest message from Alexa using OpenCV. Furthermore, I have made much progress in the logic and Blackjack farm modules, but it is still a long way from perfect. To briefly summarize my last week's progress:

1. Built a function that will crop each message, increasing OCR accuracy drastically and allowing the client to respond to and reason with specific messages (allowing for the hard-coding of context to be a lot easier, not having to rely on parsing text blocks)
2. Created a function that will log all messages received and sent
3. Started drawing up the training architecture for a simple predictive AI model that will train in 10 million simulated games of Blackjack (estimated time of training: 2 days). This will allow the client to have better long-term reasoning and gold management, as well as avoid any suspicion of automation from the developers
