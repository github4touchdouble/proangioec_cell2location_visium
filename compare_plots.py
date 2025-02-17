#!/usr/bin/env python3
import matplotlib.pyplot as plt
import cv2
import argparse


def compare_plots(plot1_file, plot2_file, plot3_file, output_file=None):
    print(f"Creating diff of {plot1_file}, {plot2_file}, and {plot3_file}...")

    # Load plots in grayscale
    plot1 = cv2.imread(plot1_file, cv2.IMREAD_GRAYSCALE)
    plot2 = cv2.imread(plot2_file, cv2.IMREAD_GRAYSCALE)
    plot3 = cv2.imread(plot3_file, cv2.IMREAD_GRAYSCALE)

    # Ensure same sizes for all plots
    if plot1.shape[:2] != plot2.shape[:2] or plot1.shape[:2] != plot3.shape[:2]:
        raise ValueError("Error: All plots must have the same dimensions.")

    # Compute absolute differences
    diff_12 = cv2.absdiff(plot1, plot2)
    diff_13 = cv2.absdiff(plot1, plot3)
    diff_23 = cv2.absdiff(plot2, plot3)

    # Invert differences for better visibility
    diff_12_inv = cv2.bitwise_not(diff_12)
    diff_13_inv = cv2.bitwise_not(diff_13)
    diff_23_inv = cv2.bitwise_not(diff_23)

    # Plot original plots and differences
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.title("Plot 1")
    plt.imshow(cv2.imread(plot1_file))
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.title("Plot 2")
    plt.imshow(cv2.imread(plot2_file))
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.title("Plot 3")
    plt.imshow(cv2.imread(plot3_file))
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.title("Diff 1-2")
    plt.imshow(diff_12_inv, cmap='gray')
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.title("Diff 1-3")
    plt.imshow(diff_13_inv, cmap='gray')
    plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.title("Diff 2-3")
    plt.imshow(diff_23_inv, cmap='gray')
    plt.axis("off")

    if output_file:
        plt.savefig(output_file)
        print(f"Plot saved to {output_file}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Create diff of three plot files. Use for same plots with different hyperparameters (specifically cells per location)."
    )
    parser.add_argument(
        "plot1", help="Path to the first plot file"
    )
    parser.add_argument(
        "plot2", help="Path to the second plot file"
    )
    parser.add_argument(
        "plot3", help="Path to the third plot file"
    )
    parser.add_argument(
        "output", help="Define the output file, usually as png", default=None
    )

    args = parser.parse_args()
    compare_plots(args.plot1, args.plot2, args.plot3, args.output)

if __name__ == "__main__":
    main()