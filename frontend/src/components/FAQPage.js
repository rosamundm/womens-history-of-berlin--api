import Navbar from "./layout/Navbar";

export default function FAQ() {

    return (
        <div class="container p-8 bg-slate-100">
            <div className="navbar">
                <Navbar />
            </div>
            <div class="p-6 text-6xl">
                FAQ
            </div>

            <div>

            <div className="q-and-a-block">
                <div class="p-4 text-4xl">
                    There's a famous Berlin street named after a princess that I can't find on here, for some reason. Why?
                </div>
                <div class="p-6 text-2xl">
                    Since there are so many such streets (among them Luisenstraße, Sophienstraße, and a surprising {''}
                    number of instances of Kaiserin-Augusta-Straße), I have decided not to include them here. {''}
                    Here is why:
                    <ul class="list-decimal p-6">
                        <li>
                            In general, I prefer not to glorify nobility. I choose to prioritise figures who earned their recognition, {''} 
                            and especially honour those who were persecuted or killed for some aspect of their beliefs or identity. 
                            <br></br>
                            Furthermore, most of these empresses and suchlike were part of the Hohenzollern dynasty, which was responsible for colonial {''}
                            crimes that Germany <i>still</i> does not acknowledge, like the {''}
                            <a href="https://www.ushmm.org/collections/bibliography/herero-and-nama-genocide"> {''}
                            genocide of the Herero and Namaqua peoples.</a>
                            <br></br>
                            For the people I <i>do</i> profile, hopefully it goes without saying that I don't necessarily agree with every single thing they {''}
                            stood for.
                            <br></br>
                            Don't bother to @ me about "erasing history". My website, my rules!
                        </li>
                        <br></br>
                        <li>
                            I don't have time to research people I find uninteresting, anyway. I work full-time and have many other projects besides this one.
                        </li>
                    </ul>
                    
                </div>
            </div>

             <div className="q-and-a-block">
                <div class="p-4 text-4xl">
                    I see a street missing. Shall I point this out to you?   
                </div>
              <div class="p-6 text-2xl">
                It might already be on my list, but: yes, feel free! If you can provide interesting sources about the {''}
                person's story, even better.
              </div>
            </div>

              <div className="q-and-a-block">
                <div class="p-4 text-4xl">
                This is sexist!
              </div>
              <div class="p-6 text-2xl">
                No.
              </div>




              


              </div>
            
            </div>
        </div>
    )
};
