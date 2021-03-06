% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/mxnet_generated.R
\name{mx.io.ImageRecordIter}
\alias{mx.io.ImageRecordIter}
\title{Create iterator for dataset packed in recordio.}
\usage{
mx.io.ImageRecordIter(...)
}
\arguments{
\item{path.imglist}{string, optional, default=''
Dataset Param: Path to image list.}

\item{path.imgrec}{string, optional, default='./data/imgrec.rec'
Dataset Param: Path to image record file.}

\item{label.width}{int, optional, default='1'
Dataset Param: How many labels for an image.}

\item{data.shape}{Shape(tuple), required
Dataset Param: Shape of each instance generated by the DataIter.}

\item{preprocess.threads}{int, optional, default='4'
Backend Param: Number of thread to do preprocessing.}

\item{verbose}{boolean, optional, default=True
Auxiliary Param: Whether to output parser information.}

\item{num.parts}{int, optional, default='1'
partition the data into multiple parts}

\item{part.index}{int, optional, default='0'
the index of the part will read}

\item{shuffle}{boolean, optional, default=False
Augmentation Param: Whether to shuffle data.}

\item{seed}{int, optional, default='0'
Augmentation Param: Random Seed.}

\item{batch.size}{int (non-negative), required
Batch Param: Batch size.}

\item{round.batch}{boolean, optional, default=True
Batch Param: Use round robin to handle overflow batch.}

\item{prefetch.buffer}{, optional, default=4
Backend Param: Number of prefetched parameters}

\item{rand.crop}{boolean, optional, default=False
Augmentation Param: Whether to random crop on the image}

\item{crop.y.start}{int, optional, default='-1'
Augmentation Param: Where to nonrandom crop on y.}

\item{crop.x.start}{int, optional, default='-1'
Augmentation Param: Where to nonrandom crop on x.}

\item{max.rotate.angle}{int, optional, default='0'
Augmentation Param: rotated randomly in [-max_rotate_angle, max_rotate_angle].}

\item{max.aspect.ratio}{float, optional, default=0
Augmentation Param: denotes the max ratio of random aspect ratio augmentation.}

\item{max.shear.ratio}{float, optional, default=0
Augmentation Param: denotes the max random shearing ratio.}

\item{max.crop.size}{int, optional, default='-1'
Augmentation Param: Maximum crop size.}

\item{min.crop.size}{int, optional, default='-1'
Augmentation Param: Minimum crop size.}

\item{max.random.scale}{float, optional, default=1
Augmentation Param: Maxmum scale ratio.}

\item{min.random.scale}{float, optional, default=1
Augmentation Param: Minimum scale ratio.}

\item{max.img.size}{float, optional, default=1e+10
Augmentation Param: Maxmum image size after resizing.}

\item{min.img.size}{float, optional, default=0
Augmentation Param: Minimum image size after resizing.}

\item{rotate}{int, optional, default='-1'
Augmentation Param: Rotate angle.}

\item{fill.value}{int, optional, default='255'
Augmentation Param: Maximum value of illumination variation.}

\item{data.shape}{Shape(tuple), required
Dataset Param: Shape of each instance generated by the DataIter.}

\item{mirror}{boolean, optional, default=False
Augmentation Param: Whether to mirror the image.}

\item{rand.mirror}{boolean, optional, default=False
Augmentation Param: Whether to mirror the image randomly.}

\item{mean.img}{string, optional, default=''
Augmentation Param: Mean Image to be subtracted.}

\item{mean.r}{float, optional, default=0
Augmentation Param: Mean value on R channel.}

\item{mean.g}{float, optional, default=0
Augmentation: Mean value on G channel.}

\item{mean.b}{float, optional, default=0
Augmentation: Mean value on B channel.}

\item{scale}{float, optional, default=1
Augmentation Param: Scale in color space.}

\item{max.random.contrast}{float, optional, default=0
Augmentation Param: Maximum ratio of contrast variation.}

\item{max.random.illumination}{float, optional, default=0
Augmentation Param: Maximum value of illumination variation.}
}
\value{
iter The result mx.dataiter
}
\description{
Create iterator for dataset packed in recordio.
}

