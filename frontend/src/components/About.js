import React, { Component } from "react";
import Navbar from "./layout/Navbar";

export default function About() {

    return (
        <div className="landing" class="px-500 justify-center justify-self-center max-w-4xl m-auto">
            <div className="navbar">
                <Navbar />
            </div>
            <div class="p-6 text-4xl">
                About
            </div>
        </div>
    )
};
