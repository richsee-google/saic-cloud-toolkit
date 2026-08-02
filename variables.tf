variable "project_id" {
  description = "Target GCP Project ID"
  type        = string
  default     = "saic-argolis-project"
}

variable "project_number" {
  description = "GCP Project Number"
  type        = string
  default     = "1234567890"
}

variable "region" {
  description = "Primary GCP Region"
  type        = string
  default     = "us-east4"
}
