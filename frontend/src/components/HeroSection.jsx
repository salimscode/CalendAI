import heroImage from '../assets/HeroImage4.svg'

const HeroSection = () => {
    return ( 
        <div className="heroSection">
            <div className="heroSectionText">
                <h1 className="heroSectionTextHeading">we make your day. </h1>
                <h4 className="heroSectionTextSubheading">the smartest calendar yet.</h4>
                <p>
                    calendai organizes your day using cai, your very own 
                    virtual calendar ai assistant. achieve more with less 
                    effort, whether you’re planning for one day or a year ahead.
                    {/* cai learns your habits and creates your
                    schedule based on priorities, suggesting the best times for meetings, 
                    focus work, and breaks. */} 
                </p>
            </div>
            <img className="heroSectionImage" src={heroImage} alt="Picture of messaging on monitor" />
        </div>
    )
}
 
export default HeroSection;