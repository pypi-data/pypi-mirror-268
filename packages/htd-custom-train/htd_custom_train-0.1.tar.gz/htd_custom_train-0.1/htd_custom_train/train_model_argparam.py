import os
import argparse
from .process_data import create_data_generators
from .train import train, save_model

def main(args):
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    
    # Load data
    train_ds, val_ds = create_data_generators(path_data=args.path_data, image_size=args.image_size, batch_size=args.batch_size)
    
    # Train model
    model = train(path=args.path_data, train_ds=train_ds, val_ds=val_ds, epochs=args.epochs)
    
    # Save model
    save_model(args.model_path, model)

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Train and save a model")
    parser.add_argument("--epochs", type=int, default=25, help="Number of epochs for training")
    parser.add_argument("--image_size", type=tuple, default=(115,115), help="The size of the image")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training")
    parser.add_argument("--path_data", type=str, default="data", help="Path to the data directory")
    parser.add_argument("--model_path", type=str, default="model.hdf5", help="Path to save the trained model")
    
    # Parse command line arguments
    args = parser.parse_args()
    
    # Run the main function
    main(args)
