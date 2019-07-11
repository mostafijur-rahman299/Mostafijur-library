# Django Request-Response life cycle


```
জ্যাংগো এর লাইফ সাইকেল কে আমরা তিনটি ভাগে ভাগ করতে পারি।

1.browser 
2 server 
3.Django

Browser : Browser সম্পর্কে আমরা নিজেরা কম বেশি অনেকে ই জানি । যার কাজ হলো server এ কোনো কিছু send করা 
          এবং সার্ভার যে তাকে জবাব দিবে তা গ্রহণ করা

Server : Browser এর থেকে একটা রিকুয়েস্ট গ্রহণ করে এবং এই পাঠানো রিকুয়েস্ট উপরে ভিত্তি করে Browser কে একটা 
         response পাঠায়।


Django: সার্ভার যখন রিকুয়েস্ট pass করে তখন Django একটা request middleware প্রয়োগ করে url এর কাছে রিকুয়েস্ট 
        send করে । url রিকুয়েস্ট এর pattern এর উপরে ভিত্তি করে views এর কাছে রিকুয়েস্ট pass করে । views তখন 
         url থেকে রিকুয়েস্ট গ্রহণ করে এবং এই রিকোয়েস্ট এর উপরে ভিত্তি করে আমরা বিভিন্ন ধরণের Django কোয়েরি এর 
         মাধ্যমে ডাটাবেস access করি। views এ আমরা আমাদের সকল ধরণের লজিক apply করি । view সব কিছু প্রসেস 
         করার পরে template কে ডাটা pass করে। template তখন প্রাসঙ্গিক ডাটা render করে , পুনরায় request middleware 
         প্রয়োগ করে Browser কে response পাঠায়।

```
