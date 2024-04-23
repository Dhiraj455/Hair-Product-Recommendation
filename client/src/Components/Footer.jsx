import React from "react";
import '../Style/Footer.css';

export default function Footer() {
    return (
        <div className="footer">
            <div className="box-container">
                <div className="box">
                    <h3> Find us here </h3>
                    <p>Shop No: 132, Main Street, Kingston, New York 12401.</p>
                    <div className="share">
                        <a href="#" className="fab fa-facebook-f"></a>
                        <a href="#" className="fab fa-twitter"></a>
                        <a href="#" className="fab fa-instagram"></a>
                        <a href="#" className="fab fa-linkedin"></a>
                    </div>
                </div>

                <div className="box">
                    <h3>contact us</h3>
                    <p>+1 (437) 243-4891</p>
                    <a href="#" className="link">
                        hairvise@gmail.com
                    </a>
                </div>

                <div className="box">
                    <h3>localization</h3>
                    <p>
                        230 Point of the Pines Dr 
                        <br />Colorado Springs 
                        <br />United State
                    </p>
                </div>
            </div>

            <div className="credit">
                created by <span>hairvise</span> | all rights reserved!
            </div>
        </div>
    );
}
