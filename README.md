YOLO implementation for detecting PCB defects using the DeepPCB dataset.

The Italian version is provided below.

DeepPCB contains 1,500 image pairs:

A defect-free template image.

A tested image with annotations for six common defect types: open, short, mousebite, spur, pin hole, and spurious copper.

Original images are very high resolution (~16k x 16k px) and are cropped into 640 x 640 px sub-images for training. Tested images are aligned to the templates using template matching and binarized to reduce illumination interference.

Each defect in the tested images is annotated with a bounding box and a class ID. Annotation files have the same name as the tested image and follow the format: x1,y1,x2,y2,type, where type is an integer from 1 to 6 corresponding to the defect class.

To run the model:

Launch pipeline_my_yolo.py, which contains the complete pipeline of scripts in order.

Results are saved in log files.

Paths to images and files can be easily modified according to your system.


Italian version:


Implementazione di YOLO per identificare difetti su PCB utilizzando il dataset DeepPCB.

DeepPCB contiene 1.500 coppie di immagini:

Una immagine di template senza difetti.

Una immagine testata con annotazioni per sei tipi di difetti comuni: open, short, mousebite, spur, pin hole e spurious copper.

Le immagini originali hanno risoluzione molto alta (~16k x 16k px) e vengono suddivise in sottoparti da 640 x 640 px per l’addestramento. Le immagini testate sono allineate ai template tramite tecniche di template matching e binarizzate per ridurre le interferenze di illuminazione.

Ogni difetto nelle immagini testate è annotato con una bounding box e un ID di classe. I file di annotazione hanno lo stesso nome dell’immagine testata e indicano: x1,y1,x2,y2,type, dove type è un numero tra 1 e 6 corrispondente al tipo di difetto.

Per eseguire il modello:

Lanciare pipeline_my_yolo.py, che contiene la pipeline completa degli script in ordine.

I risultati vengono salvati in file di log.

I percorsi delle immagini e dei file possono essere modificati facilmente in base al proprio PC.