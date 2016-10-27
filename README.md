# fire-effect
A fire effect for your Halloween pumpkin using a Pimoroni Blinkt!
If you’d like to create your own pumpkin light effect, you'll need:
<ul>
 	<li>A Raspberry Pi (Make sure you use one that fits in your pumpkin!)</li>
 	<li><a href="https://shop.pimoroni.com/products/blinkt">A Pimoroni Blinkt!</a></li>
 	<li>A power supply (plus monitor, mouse, and keyboard for setup)</li>
 	<li>A pumpkin</li>
</ul>
<p class="p1"><span class="s1">Take your Blinkt! and attach it to your Pi. If you’re using a 1-3 model, this will be easy enough, but make sure the Pi fits in your pumpkin! If, like me, you need to go smaller, you’ll have to solder your header pins to a Zero before attaching the HAT.</span></p>
<p class="p1"><span class="s1">You might want to make sure Raspbian is running on the newest version. Why? Well, why not? You don’t have to upgrade to <a href="https://www.raspberrypi.org/blog/introducing-pixel/">PIXEL,</a> but you totally should as it’s very pretty. Its creator, <a href="https://twitter.com/simonlong_rpi">Simon Long</a>, was my soldering master for this project. His skills are second to none. To upgrade to Pixel, follow the steps <a href="https://www.raspberrypi.org/blog/introducing-pixel/">here</a>.</span></p>
<p class="p1"><span class="s1">In the terminal, you’ll need to install <a href="https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt">the Pimoroni Blinkt! library</a>. Use the following to achieve this:</span></p>

<pre>curl -sS get.pimoroni.com/blinkt | bash</pre>
You'll need to reboot the Raspberry Pi to allow the changes to take effect. You can do this by typing:
<pre>sudo reboot</pre>
<p class="p1"><span class="s1">At this point, you’re more than welcome to go your own way with the <a href="https://shop.pimoroni.com/products/blinkt">Blinkt!</a> and design your own light show (<a href="https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt">this may help</a>). However, and with major thanks to <a href="https://twitter.com/jonic">Jonic Linley</a>, we’ve created a pumpkin fire effect for you.</span></p>
<p class="p1"><span class="s1">Within the terminal, type:</span></p>

<pre>git clone https://github.com/AlexJrassic/fire_effect.git</pre>
This will bring the code to your Raspberry Pi from GitHub. Next, we need to tell the Raspberry Pi to automatically start the fire_effect.py code when you power up. To do this, type:
<pre>nano ~/.config/lxsession/LXDE-pi/autostart</pre>
At end of the file, add this line:
<pre>@python /home/pi/fire_effect/fire_effect.py</pre>
Save and then reboot:
<pre>sudo reboot
</pre>
<p class="p1"><span class="s1">Now you’re good to go. </span></p>
<p class="p1"><img class="aligncenter wp-image-26300 size-large" src="/wp-content/uploads/2016/10/IMG_9917-e1477571770975-500x500.jpg" alt="Halloween Pumpkin AFTER" width="500" height="500" /></p>
<p class="p1"><span class="s1">To add more of a spread to the light effect, I created a diffuser to cover the Blinkt! LEDs. In the video (https://www.youtube.com/watch?v=YrlezeYjdu0), you’ll see I used a tissue. I wouldn’t suggest this for prolonged use, due to the unit getting a little warm; I won’t be responsible for any  subsequent tissue fires. I would suggest using a semi-opaque bowl (the ones you get a Christmas pudding in) or a piece of plastic from a drinks bottle, and go to town on it with some fine sandpaper.</span></p>
<p class="p1">We also drilled a small hole in the back for the micro-USB lead to reach the Zero. I used a battery pack for power, but you could use a lead directly into the mains. With a larger pumpkin, you could put a battery pack inside with the Pi.</p>
